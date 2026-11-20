def verify_while(correct_otp, entries):
    attempts = 0
    for entry in entries:
        if entry == "":
            print("Blank entry: not counted")
            continue
        attempts += 1
        if entry == correct_otp:
            print("OTP verified")
            break
        print("Wrong OTP")
        if attempts == 3:
            print("Account locked for 30 minutes")
            break
    else:
        if attempts < 3:
            print("Attempts finished without lock")

def verify_for(correct_otp, entries):
    attempts = 0
    for entry in entries[:3]:
        if entry == "":
            print("Blank entry: not counted")
            continue
        attempts += 1
        if entry == correct_otp:
            print("OTP verified")
            break
        print("Wrong OTP")
    else:
        if attempts == 3:
            print("Account locked for 30 minutes")
        else:
            pass  # No additional action for unused attempts.

print("WHILE-style demonstration:")
verify_while("4821", ["", "1111", "2222", "3333"])
print("\nFOR-style demonstration:")
verify_for("4821", ["", "1111", "2222", "3333"])
print("\nChanged condition: after a correct security answer, set maximum attempts to 5.")
