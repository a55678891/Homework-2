from itertools import permutations

liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

def get_trade_output(amount_in, token_in, token_out, liquidity):
    key = (token_in, token_out) if (token_in, token_out) in liquidity else (token_out, token_in)
    reserve_in, reserve_out = liquidity[key]

    if (token_in, token_out) not in liquidity:
        reserve_in, reserve_out = reserve_out, reserve_in

    amount_out = reserve_out * amount_in / (reserve_in + amount_in)
    return amount_out

def find_profitable_arbitrage(start_token, liquidity, initial_amount):
    tokens = list(set([token for pair in liquidity.keys() for token in pair]))
    tokens.remove(start_token)

    profitable_paths = []
    for perm in permutations(tokens):
        current_amount = initial_amount
        path = [start_token] + list(perm) + [start_token]
        for i in range(len(path)-1):
            current_amount = get_trade_output(current_amount, path[i], path[i+1], liquidity)
            if current_amount <= 0:
                break
        if current_amount > 20:
            profitable_paths.append((path, current_amount))
            
    return profitable_paths

def format_path_output(profitable_paths):
    if not profitable_paths:
        return "No profitable path found."
    
    best_path = max(profitable_paths, key=lambda x: x[1])
    path_string = "->".join(best_path[0])
    balance = best_path[1]
    return f"path: {path_string}, tokenB balance={balance:.6f}"

profitable_paths = find_profitable_arbitrage('tokenB', liquidity, 5)
formatted_output = format_path_output(profitable_paths)
print(formatted_output)
