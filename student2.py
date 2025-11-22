import sys

if len(sys.argv) == 3:
  script_name = sys.argv[0]
  name = sys.argv[2]
  print("user provided input value:")
else:
  script_name = sys.argv[0]
  name = "Basamma"
  rollno = "251"
  print("no input given -using default values:")

print("script name:",script_name)
print("Student name:",name)
print("Roll number:",rollno)
