import openai 

# Replace with your OpenAI API key
openai.api_key = ""

def generate_keywords(text):
  """
  This function takes a block of text and returns a list of keywords extracted from the text, categorized into category, sub-category, and other keywords.

  Args:
    text: A string containing the text to extract keywords from.

  Returns:
    A list of lists containing the extracted keywords, categorized into category, sub-category, and other keywords.
  """

  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system",
        "content": "You will be provided with a item Name, and your task is to extract a  list of keywords from it and identify a single(must) category(ex: Electronics,Household,Automobile), a single(must) sub category(Ex:Smart phone,Microwave,Tyre) and other kewords (can be multiple).Seperate by commas"
      },
      {
        "role": "user",
        "content": text
      }
    ],
    temperature=1,
    max_tokens=64,
    top_p=1
  )

  keywords = response.choices[0].message.content.split("\n")
  stripped_keywords = [keyword.strip() for keyword in keywords]

  categories = []
  sub_categories = []
  other_keywords = []

  for keyword in stripped_keywords:
    if "Category:" in keyword:
      categories.append(keyword.split(":")[1])
    elif "Subcategory:" in keyword:
      sub_categories.append(keyword.split(":")[1])
    elif "Keywords:" in keyword:
      print (keyword)
      try:
        other_keywords.append(keyword.split(",")[1])
      except Exception as e:
        print(e)
    # else:
      other_keywords.append(keyword)
# stripped_keywords = [keyword.strip() for keyword in keywords]
  return [category.strip() for category in categories], [subcategory.strip() for subcategory in sub_categories] ,[kw.strip() for kw in other_keywords] 

# Example usage
# text = "Samsung WB150F Smart Digital WiFi Compact Camera Black 14.2MP 18X Zoom BLK"
# categories, sub_categories, other_keywords = generate_keywords(text)

# print("Categories:", categories)
# print("Sub-Categories:", sub_categories)
# print("Other Keywords:", other_keywords)