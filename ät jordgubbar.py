print("Välkommen till Ät Jordgubbar! \n")
print("Ät jordgubbar, men var försiktig. \n")
print("Under spelets gång kommer du att mötas av många jordgubbar men alla är inte goda.")
print("Skriv ja om du vill äta jordgubben och nej om du inte vill det")
print("----------------------------------")
for i in range(100):
    print("Du vaknar upp ute i skogen och tittar upp mot molnen, och känner dig lite hungrig.")
    val = str(input("Vill du ligga kvar eller köpa Jordgubbar"))
    if val == "ligga kvar":
        print("Du somnar")
    if val == "köpa":
        print("Du köper nyplockade Belgiska jordgubbar och somnar")

