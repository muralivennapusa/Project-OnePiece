import requests
from bs4 import BeautifulSoup


def get_text_from_webpage(url):
    # Fetch the webpage content
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes
    
    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract text from the parsed HTML
    text = soup.get_text(separator='\n', strip=True)
    
    

    return text

# Example usage
url = 'https://onepiece.fandom.com/wiki/Episode_'
l=[]
for i in range(3,31):
    u=url+str(i)
    text = get_text_from_webpage(u)
    r=text.split("Long Summary")[-1]
    r=text.split("Characters in Order")[-2]
    txt=text.split("Long Summary")[-1]
    res=txt.split("Characters in Order")[0]
    l.append(' '.join(res.split("\n")))
    print("Extracted episode ",i)

#print(" ".join(res.split("\n")))
#print(*l,sep='\n episode st')

print("Extraction complete till ",len(l))

c=0

with open("EpCount.txt",'r') as file:
    c=file.read()
c=int(c)
with open("onepiece.txt",'a') as file:
    for i in range(len(l)):
        file.write(f"\n\nEpisode {c+1}\n\n")
        c=c+1
        file.write(l[i][4:])
print("Written to file")

with open("EpCount.txt",'w') as file:
    file.write(str(c))
print("Updated count")