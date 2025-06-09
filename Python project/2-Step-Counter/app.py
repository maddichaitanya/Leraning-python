print("🚶➡️   STEP COUNTER 🚶➡️")
try:
    step = int(input(" 🎯 What is your daily step goal ! 🎯 : "))
    output = int(input("✨✨ Who many steps you have taken ✨✨ : "))
    result = output-step
    result1 = step-output
    if step < output:
        print(f" 🎉 👏 congratulations You have completed your Goal by {result} Steps 🎉 👏")
    elif step == output:
        print("🎉 👏 congratulations You have completed your Goal Steps 🎉 👏")
    else:
        print(f" 💪 You need {result1} more steps to complete your goal ! 💪")
except ValueError:
    print("🎯 Wrong Input 🎯 ")
