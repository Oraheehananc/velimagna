from rich import print

def approve_delegation(web3, radiant, tx_token):
    """Approves the delegation of the token to the radiant contract.

    Args:
        web3 (Web3): Web3 instance.
        radiant (Contract): Radiant contract instance.
        tx_token (str): Transaction hash of the token approval.
    """

    print(f'\n>>> approve_delegation radiant | https://www.example.com ', 'green')

