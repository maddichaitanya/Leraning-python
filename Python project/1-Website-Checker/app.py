print("🔎  WEBSITE URL CHECKER  🔎")

url = input("\nEnter a Website URL : ")

if url.startswith("https://"):
    print("\n🔐 This Website uses URL HTTPS ( Secure 🔐 )")
elif url.startswith("http://"):
    print("\n🔓 This Website uses URL HTTP ( not Secure 🔓 )")
else:
    print("\n❌ Enter URL is not valide : ❌")

# Output link :- https://app.eraser.io/workspace/2ljwCmd4iskZQrkBaitg?origin=
