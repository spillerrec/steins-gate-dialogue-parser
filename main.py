from html.parser import HTMLParser
import json

items = []

class MyHTMLParser(HTMLParser):
	def __init__(self):
		super().__init__()
		self.add_to_last = False
		self.ignore_lines = False
		
	def addToItem(self, text):
		if self.add_to_last:
			items[-1]['text'] = items[-1]['text'] + text
			self.add_to_last = False
		else:
			items.append({'text': text})
	
	def handle_tag_shared(self, tag):
		if tag == 'i':
			self.add_to_last = True
			self.addToItem('*')
			self.add_to_last = True
		elif tag in ['font', 'center', 'chaptername', 'move', 'k']:
			self.add_to_last = True
		elif tag != 'pre':
			print("Encountered a start tag:", tag)
	
	def handle_starttag(self, tag, attrs):
		if tag == 'voice':
			items.append({
					'char': attrs[0][1],
					'text': ''
				})
			self.add_to_last = True
		elif tag == 'call':
			self.ignore_lines = True
		else:
			self.handle_tag_shared(tag)

	def handle_endtag(self, tag):
		if tag == 'call':
			self.ignore_lines = False
		else:
			self.handle_tag_shared(tag)

	def handle_data(self, data):
		if not self.ignore_lines:
			lines = data.split('\n')
			for line in lines:
				if line:
					if line[0] != '[' and line[-1] != ']':
						self.addToItem(line)

with open('Master_Copy.txt', encoding="utf-8") as f:
	parser = MyHTMLParser()
	parser.feed(f.read())
	
print(len(items))

with open('parsed.json', "w") as f:
	json.dump(items, f, indent=2)