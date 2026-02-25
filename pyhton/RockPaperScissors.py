import random

rock1="👊👊👊👊👊👊👊"

peper1="✋✋✋✋✋✋✋"

makas1="✌️✌️✌️✌️✌️✌️✌️"

print("\n welcome to gaim ")

compinm=input(" in not (Help)").lower()

if compinm=="help":
	
	print("انت الان في لعب حجر ورقة مقص المقص يفوز على الورقة والورقة تفوز على الحجر والحجر تفوز على المقص")
	
usee1=input(" enter the (rock,peper,makas)\n")


if usee1 not in ["rock","peper","makas"]:
	
	print(" sore nnnnnnn")
	
else:
	
	if usee1=="rock":
		print(f"\n te is\n{rock1}")
		
	elif usee1=="peper":
		print(f"\n te is\n{peper1} ")
		
		
	else:
		print(f"\n te is \n{makas1}")
	
coputer=random.choice(["rock","peper","makas"])

if coputer=="rock":
	print(f"\n computer is \n{rock1}")
	
elif coputer=="peper":
	print(f"\n computr is\n {peper1}")

else:
	print(f"\n computre\n {makas1}")
	
	
if usee1==coputer:
	print("50 es 50 **&& ")
	
elif(
(usee1=="rock" and coputer=="makas")or (usee1=="peper" and coputer=="rock")or (usee1=="makas" and coputer=="peper" )):
	print(f"you win {usee1} bat {coputer}. ")
	
else:
	print(f" yeu lese {usee1}  bat {coputer}")
	
		
	
	
	
	
	



