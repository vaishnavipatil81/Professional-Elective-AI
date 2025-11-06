# Expert System: Daily Routine Adviser

print("=== Daily Routine Adviser Expert System ===\n")

sleep = float(input("How many hours do you sleep per day? "))
breakfast = input("Do you eat breakfast daily? (yes/no): ").lower()
exercise = input("Do you exercise regularly? (yes/no): ").lower()
screen_time = float(input("How many hours do you spend on screens daily? "))
stress = input("Do you feel stressed often? (yes/no): ").lower()
relax = input("Do you take time for relaxation or hobbies? (yes/no): ").lower()
meals = input("Do you eat lunch and dinner on time? (yes/no): ").lower()

print("\nAnalyzing your routine...\n")

# Sleep analysis
if sleep < 6:
    print("🛏 You’re not sleeping enough! Aim for 7–8 hours of sleep.")
elif 6 <= sleep <= 8:
    print("😴 Great! You’re getting good rest.")
else:
    print("⚠ Oversleeping may reduce productivity. Try 7–8 hours.")

# Breakfast
if breakfast == "no":
    print("🍳 Don’t skip breakfast — it boosts energy for the day.")
else:
    print("✅ Good! Breakfast helps maintain focus.")

# Exercise
if exercise == "no":
    print("🏃 Include 30 minutes of physical activity daily.")
else:
    print("💪 Regular exercise keeps you active and healthy.")

# Screen time
if screen_time > 6:
    print("📱 Too much screen time! Take short breaks every hour.")
elif 3 <= screen_time <= 6:
    print("🖥 Moderate screen use — try balancing with outdoor time.")
else:
    print("🌿 Excellent! Healthy screen usage.")

# Stress
if stress == "yes":
    print("🧘 Try relaxation techniques like meditation or music.")
else:
    print("😊 Great! Keep managing your stress well.")

# Relaxation or hobby time
if relax == "no":
    print("🎨 Add some leisure or hobby time for mental balance.")
else:
    print("🌈 Having hobbies helps maintain happiness and creativity.")

# Meals
if meals == "no":
    print("🍽 Try to eat your meals on time to avoid fatigue.")
else:
    print("🥗 Regular meals support stable energy levels.")

# Final summary
if (
    6 <= sleep <= 8 and
    breakfast == "yes" and
    exercise == "yes" and
    screen_time <= 6 and
    stress == "no" and
    relax == "yes" and
    meals == "yes"
):
    print("\n🌟 Summary: Excellent daily routine! Keep it up 👍")
else:
    print("\n🩺 Summary: Improve a few habits for a balanced and healthy lifestyle.")
