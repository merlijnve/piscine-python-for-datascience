import time

seconds = time.time()
time_struct = time.gmtime()
print("Seconds since January 1, 1970: " + f'{seconds:,.4f}' + " or " + f'{seconds:,.2e}' + " in scientific notation")
print(time.strftime("%b %d %Y", time_struct))