import os
from dotenv import load_dotenv
from openapi_client import openapi
from openapi_genclient import PortfolioPosition
from tinkoff.invest import Client, PositionsResponse

load_dotenv()

TOKEN = os.getenv('TOKEN')

def main():
    with Client(TOKEN) as client:
        account = client.users.get_accounts().accounts[0].id
        positions: PositionsResponse = client.operations.get_portfolio(account_id=account)
        print(positions.positions)

if __name__ == "__main__":
    main()