amount_audience = int(input())

oscars = amount_audience * 0.7
catering = oscars * 0.85
sounds = catering * 0.5

total_amount = oscars + catering + sounds + amount_audience

print(f"{total_amount:.2f}")
