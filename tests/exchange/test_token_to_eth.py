def test_swap_all(t, chain, uni_token, uni_exchange, assert_tx_failed):
    deadline = chain.head_state.timestamp + 300
    uni_token.transfer(t.a1, 2*10**18)
    uni_token.approve(uni_exchange.address, 10*10**18)
    uni_token.approve(uni_exchange.address, 2*10**18, sender=t.k1)
    uni_exchange.addLiquidity(10*10**18, deadline, value=5*10**18)
    # Starting balances of UNI exchange
    assert chain.head_state.get_balance(uni_exchange.address) == 5*10**18
    assert uni_token.balanceOf(uni_exchange.address) == 10*10**18
    # Starting balances of BUYER
    assert uni_token.balanceOf(t.a1) == 2*10**18
    assert chain.head_state.get_balance(t.a1) == 1*10**24
    # BUYER converts ETH to UNI
    uni_exchange.tokenToEthSwap(2*10**18, 1, deadline, sender=t.k1)
    # Updated balances of UNI exchange
    assert chain.head_state.get_balance(uni_exchange.address) == 4168403501458941225
    assert uni_token.balanceOf(uni_exchange.address) == 12*10**18
    # Updated balances of BUYER
    assert uni_token.balanceOf(t.a1) == 0
    assert chain.head_state.get_balance(t.a1) == 1*10**24 + 831596498541058775

def test_swap_exact(t, chain, uni_token, uni_exchange, assert_tx_failed):
    deadline = chain.head_state.timestamp + 300
    uni_token.transfer(t.a1, 3*10**18)
    uni_token.approve(uni_exchange.address, 10*10**18)
    uni_token.approve(uni_exchange.address, 3*10**18, sender=t.k1)
    uni_exchange.addLiquidity(10*10**18, deadline, value=5*10**18)
    # Starting balances of UNI exchange
    assert chain.head_state.get_balance(uni_exchange.address) == 5*10**18
    assert uni_token.balanceOf(uni_exchange.address) == 10*10**18
    # Starting balances of BUYER
    assert uni_token.balanceOf(t.a1) == 3*10**18
    assert chain.head_state.get_balance(t.a1) == 1*10**24
    # BUYER converts ETH to UNI
    uni_exchange.tokenToEthSwapExact(3*10**18, 831596498541058775, deadline, sender=t.k1)
    # Updated balances of UNI exchange
    assert chain.head_state.get_balance(uni_exchange.address) == 4168403501458941225
    assert uni_token.balanceOf(uni_exchange.address) == 12*10**18 + 1         # Exchange gets 1 more token due to fee rounding
    # Updated balances of BUYER
    assert uni_token.balanceOf(t.a1) == 1*10**18 - 1
    assert chain.head_state.get_balance(t.a1) == 1*10**24 + 831596498541058775

def test_transfer_all(t, chain, uni_token, uni_exchange, assert_tx_failed):
    deadline = chain.head_state.timestamp + 300
    uni_token.transfer(t.a1, 2*10**18)
    uni_token.approve(uni_exchange.address, 10*10**18)
    uni_token.approve(uni_exchange.address, 2*10**18, sender=t.k1)
    uni_exchange.addLiquidity(10*10**18, deadline, value=5*10**18)
    # Starting balances of UNI exchange
    assert chain.head_state.get_balance(uni_exchange.address) == 5*10**18
    assert uni_token.balanceOf(uni_exchange.address) == 10*10**18
    # Starting balances of BUYER
    assert uni_token.balanceOf(t.a1) == 2*10**18
    assert chain.head_state.get_balance(t.a1) == 1*10**24
    # Starting balances of RECIPIENT
    assert uni_token.balanceOf(t.a2) == 0
    assert chain.head_state.get_balance(t.a2) == 1*10**24
    # BUYER converts ETH to UNI
    uni_exchange.tokenToEthTransfer(t.a2, 2*10**18, 1, deadline, sender=t.k1)
    # Updated balances of UNI exchange
    assert chain.head_state.get_balance(uni_exchange.address) == 4168403501458941225
    assert uni_token.balanceOf(uni_exchange.address) == 12*10**18
    # Updated balances of BUYER
    assert uni_token.balanceOf(t.a1) == 0
    assert chain.head_state.get_balance(t.a1) == 1*10**24
    # Updated balances of RECIPIENT
    assert uni_token.balanceOf(t.a2) == 0
    assert chain.head_state.get_balance(t.a2) == 1*10**24 + 831596498541058775

def test_transfer_exact(t, chain, uni_token, uni_exchange, assert_tx_failed):
    deadline = chain.head_state.timestamp + 300
    uni_token.transfer(t.a1, 3*10**18)
    uni_token.approve(uni_exchange.address, 10*10**18)
    uni_token.approve(uni_exchange.address, 3*10**18, sender=t.k1)
    uni_exchange.addLiquidity(10*10**18, deadline, value=5*10**18)
    # Starting balances of UNI exchange
    assert chain.head_state.get_balance(uni_exchange.address) == 5*10**18
    assert uni_token.balanceOf(uni_exchange.address) == 10*10**18
    # Starting balances of BUYER
    assert uni_token.balanceOf(t.a1) == 3*10**18
    assert chain.head_state.get_balance(t.a1) == 1*10**24
    # Starting balances of RECIPIENT
    assert uni_token.balanceOf(t.a2) == 0
    assert chain.head_state.get_balance(t.a2) == 1*10**24
    # BUYER converts ETH to UNI
    uni_exchange.tokenToEthTransferExact(t.a2, 3*10**18, 831596498541058775, deadline, sender=t.k1)
    # Updated balances of UNI exchange
    assert chain.head_state.get_balance(uni_exchange.address) == 4168403501458941225
    assert uni_token.balanceOf(uni_exchange.address) == 12*10**18 + 1
    # Updated balances of BUYER
    assert uni_token.balanceOf(t.a1) == 1*10**18 - 1
    assert chain.head_state.get_balance(t.a1) == 1*10**24
    # Updated balances of RECIPIENT
    assert uni_token.balanceOf(t.a2) == 0
    assert chain.head_state.get_balance(t.a2) == 1*10**24 + 831596498541058775
