import sys
import asyncio
from rich.console import Console
from rich.table import Table

# Import helpers from checker.py
from checker import check_all_domains, clean_and_expand_domain

console = Console()

def print_table(results: list[dict]):
    table = Table(title="🔍 Fast Domain Checker Results", header_style="bold cyan")
    table.add_column("Domain", style="bold white")
    table.add_column("Status", justify="center")
    table.add_column("Active DNS", justify="center")
    table.add_column("Registered", justify="center")

    for r in results:
        if r["status"] == "TAKEN":
            status_style = "[bold red]TAKEN[/bold red]"
        elif r["status"] == "AVAILABLE":
            status_style = "[bold green]AVAILABLE[/bold green]"
        else:
            status_style = f"[bold yellow]{r['status']}[/bold yellow]"

        dns_style = "✅ Yes" if r["has_active_dns"] else "❌ No"
        reg_style = "✅ Yes" if r["is_registered"] else "❌ No"

        table.add_row(r["domain"], status_style, dns_style, reg_style)

    console.print(table)

def main():
    console.print("[bold blue]=====================================[/bold blue]")
    console.print("[bold blue] 🌐 Async Domain Checker CLI   [/bold blue]")
    console.print("[bold blue]=====================================[/bold blue]")
    console.print("[dim]Type 'exit' or 'q' anytime to quit.[/dim]\n")

    while True:
        try:
            console.print("[bold yellow]👉 Enter domain or brand name:[/bold yellow]")
            user_input = input("> ").strip()

            if not user_input:
                continue

            if user_input.lower() in ['exit', 'quit', 'q']:
                console.print("\n[bold cyan]Goodbye! 👋[/bold cyan]")
                sys.exit(0)

            raw_tokens = user_input.replace(",", " ").split()
            domains_to_check = []
            for token in raw_tokens:
                domains_to_check.extend(clean_and_expand_domain(token))

            if domains_to_check:
                with console.status("[bold green]Checking domains asynchronously...[/bold green]"):
                    results = asyncio.run(check_all_domains(domains_to_check))
                print_table(results)
                console.print("\n" + "─"*50 + "\n")

        except (KeyboardInterrupt, EOFError):
            console.print("\n[bold cyan]Goodbye! 👋[/bold cyan]")
            sys.exit(0)

if __name__ == "__main__":
    main()