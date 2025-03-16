from .models import WalletMonthlySummary


def get_previous_year_month(year, month) -> list[int, int]:
    return (year - 1 if month == 1 else year, month - 1 if month > 1 else 12)


def get_previous_wallet_summary(wallet, year, month):
    prev_year, prev_month = get_previous_year_month(year, month)

    return WalletMonthlySummary.objects.filter(
        wallet=wallet, year=prev_year, month=prev_month
    ).first()
