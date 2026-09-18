import asyncio
import httpx
import dns.asyncresolver

DEFAULT_TLDS = [".com", ".net", ".io", ".ma"]

def clean_and_expand_domain(raw_input: str) -> list[str]:
    """Clean input and automatically add TLDs if missing."""
    clean = raw_input.strip().lower()
    clean = clean.replace("https://", "").replace("http://", "").replace("www.", "").split("/")[0]
    
    if not clean:
        return []

    if "." not in clean:
        return [f"{clean}{tld}" for tld in DEFAULT_TLDS]
    return [clean]

async def check_single_domain(client: httpx.AsyncClient, domain: str) -> dict:
    result = {"domain": domain, "is_registered": False, "has_active_dns": False, "status": "UNKNOWN"}
    
    # 1. Async DNS Check
    try:
        resolver = dns.asyncresolver.Resolver()
        resolver.lifetime = 2.0
        await resolver.resolve(domain, 'NS')
        result["has_active_dns"] = True
    except Exception:
        pass

    # 2. Async RDAP HTTP Check
    try:
        res = await client.get(f"https://rdap.org/domain/{domain}", timeout=4.0)
        if res.status_code == 200:
            result["is_registered"] = True
            result["status"] = "TAKEN"
        elif res.status_code == 404:
            result["status"] = "AVAILABLE"
        else:
            result["status"] = f"HTTP_{res.status_code}"
    except httpx.TimeoutException:
        result["status"] = "TIMEOUT"
    except Exception:
        result["status"] = "ERROR"

    return result

async def check_all_domains(domains: list[str]) -> list[dict]:
    """Execute all checks concurrently in parallel."""
    async with httpx.AsyncClient(follow_redirects=True) as client:
        tasks = [check_single_domain(client, d) for d in domains]
        return await asyncio.gather(*tasks)