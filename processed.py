import json

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
    return {
        'line count': 2,
        'language': 'English',
        'tags': ['Internship', 'Career', 'Milestone']

        
    }
          
if __name__ == "__main__":
    process_json("data/raw_posts.json", "data/pre_processsed.json")