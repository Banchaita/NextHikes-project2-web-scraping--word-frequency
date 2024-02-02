import requests
from bs4 import BeautifulSoup
from bs4 import NavigableString
#  Create new html file
def fetchAndSaveToFile(url, path):
    try:
        r = requests.get(url)
        r.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(r.text)
        
        print(f"Content successfully saved to {path}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

url = 'https://www.python.org/'
fetchAndSaveToFile(url, "data/task.html")

# # Content get of url
r = requests.get(url)
print("content get of url====",r.content[:100])


# get and open html file

with open("data/task.html", "r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')
# get all document
print("soup",soup.prettify())

# Get title
print(soup.title, type(soup.title))
# get title name
print(soup.title.name, type(soup.title.name))
# get title string
print(soup.title.string, type(soup.title.string))

# get div
print(soup.div)
# get all div 
print(type(soup.find_all("div")[6]))

# get all links

for link in soup.find_all("a"):
    print("Getting Linking----->>>>>>>>",link.get("href"))
    print("Getting Linking Text--------",link.get_text())

s = soup.find(id="link3")
print(s.get("href"))

# Get div class
print("Get div class---->>>>>>>",soup.select("div.header-banner"))


# get div id
print("get div id---->>>>>>>",soup.select("div#touchnav-wrapper"))

# get span class

print("get span class------",soup.span.get("class"))

# get fine all some class
print("get fine all some class========",soup.find(class_="slide-copy"))

# Get Child content
for child in soup.find(class_="container").children:
    print("Get Child contect********",child)

# Get parent content

i = 0
for parent in soup.find(class_="options-bar").parents:
    i +=1
    print("Get parent content====",parent)
    if(i ==2):
      break

# Cont of class

cont = soup.find(class_="container")
cont.name = "span"
cont["class"] = "slide-copy"
cont.string = "Experienced programmers"
print("cont****",cont)


# Inster new ul and li tag
def fetchAndSaveToFile(url, path):
    try:
        r = requests.get(url)
        r.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        
        soup = BeautifulSoup(r.text, 'html.parser')
        
        ulTag = soup.new_tag("ul")
        liTag = soup.new_tag("li")
        liTag.string = "Home"
        ulTag.append(liTag)

        liTag = soup.new_tag("li")
        liTag.string = "About"
        ulTag.append(liTag)

        liTag = soup.new_tag("li")
        liTag.string = "Service"
        ulTag.append(liTag)

        soup.html.body.insert(0, ulTag)
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(str(soup))
        
        print(f"Content successfully saved to {path}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

url = 'https://www.python.org/'
fetchAndSaveToFile(url, "data/modified.html")

def has_class_but_not_id(tag):
    # return tag.has_attr("class") and not tag.has_attr("id")
    return  not tag.has_attr("class") and not tag.has_attr("id")

def has_content(tag):
    return tag.has_attr("content")

results = soup.find_all(has_class_but_not_id)
print("results---",results)

for result in results:
    print("result==>>>","\n\n",result)


for string in soup.stripped_strings:
    print(repr(string))

sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></a>", 'html.parser')
print(sibling_soup.prettify())

def surrounded_by_strings(tag):
    return (isinstance(tag.next_element, NavigableString)
            and isinstance(tag.previous_element, NavigableString))

for tag in soup.find_all(surrounded_by_strings):
    print(tag.name)


def has_six_characters(css_class):
    return css_class is not None and len(css_class) == 6

print(soup.find_all(class_=has_six_characters))

print(soup.css.select("head > title"))
print(soup.css.select("p > a"))
print(soup.css.select("p > a:nth-of-type(2)"))
print(soup.css.select("body > a"))

print(soup.css.select(".sitemap"))
