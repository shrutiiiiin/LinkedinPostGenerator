import json
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from llm_helper import llm

def process_json(raw_file_path, processed_file_path ="data/pre_processsed.json") :
    enriched_posts = []
    with open(raw_file_path, encoding="utf-8") as file:
        posts = json.load(file)
        # print(posts)
        for post in posts:
            metadata = extract_metadata(post['text'])
            post_with_metadata = post | metadata
            enriched_posts.append(post_with_metadata)
            
    for epost in enriched_posts:
        print (epost)
        
        
def extract_metadata(post):
    template = '''
    You are given a LinkedIn post. You need to extract number of lines, language of the post and tags.
    1. Return a valid JSON. No preamble. 
    2. JSON object should have exactly three keys: line_count, language and tags. 
    3. tags is an array of text tags. Extract maximum two tags.
    4. Language should be English or Hinglish (Hinglish means hindi + english)
    
    Here is the actual post on which you need to perform this task:  
    {post}
    '''
    
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={'post': post})
    
    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
        print("Raw LLM response:", response.content)

    except OutputParserException:
        raise OutputParserException("Context too big, unable to parse jobs")
    return res
        
 
if __name__ == "__main__":
    process_json("data/raw_posts.json", "data/pre_processsed.json")