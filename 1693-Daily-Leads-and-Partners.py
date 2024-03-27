import pandas as pd


def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    num_leads = daily_sales[['date_id', 'make_name', 'lead_id']].drop_duplicates().groupby(['date_id', 'make_name'])['lead_id'].count().reset_index()
    num_partners = daily_sales[['date_id', 'make_name', 'partner_id']].drop_duplicates().groupby(['date_id', 'make_name'])['partner_id'].count().reset_index()

    return pd.merge(num_leads, num_partners, on=['date_id', 'make_name']).rename(columns={'lead_id': 'unique_leads', 'partner_id': 'unique_partners'})


# Performance Result:
#   Coding Time: 00:06:37
#   Time Complexity: O(N)
#   Space Complexity: O(N)
#   Runtime: 853 ms, faster than 25.33%
#   Memory Usage: 68.13 MB, less than 5.75%
