import json

d = {
	"alma":"apple",
	"korte":"pear"

}
print(json.dumps(d))
with open("dump-json1","w") as js:
	json.dump(d,js)
