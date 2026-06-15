SKILLS_DB = [

    # Programming Languages
    "python", "java", "javascript", "typescript",
    "c", "c++", "c#", "go", "ruby", "php",
    "kotlin", "swift", "r", "scala",

    # Frontend
    "html", "css", "bootstrap", "tailwind",
    "react", "next.js", "angular", "vue.js",
    "redux", "jquery",

    # Backend
    "node.js", "express.js", "django", "flask",
    "fastapi", "spring boot", "hibernate",
    "ruby on rails", "laravel", ".net",
    "asp.net",

    # Databases
    "sql", "mysql", "postgresql", "mongodb",
    "sqlite", "oracle", "redis", "cassandra",
    "firebase", "dynamodb",

    # AI / ML / Data Science
    "machine learning", "deep learning",
    "artificial intelligence", "nlp",
    "computer vision", "tensorflow",
    "pytorch", "keras", "scikit-learn",
    "pandas", "numpy", "matplotlib",
    "seaborn", "xgboost", "opencv",
    "llm", "transformers", "hugging face",

    # Data Engineering
    "apache spark", "hadoop", "airflow",
    "etl", "data warehouse", "kafka",

    # DevOps & Cloud
    "docker", "kubernetes", "jenkins",
    "github actions", "terraform",
    "aws", "azure", "gcp",
    "linux", "nginx",

    # Mobile Development
    "android", "ios", "flutter",
    "react native", "swift", "kotlin",

    # Testing
    "pytest", "rspec", "junit",
    "selenium", "cypress", "postman",

    # Version Control
    "git", "github", "gitlab", "bitbucket",

    # APIs
    "rest api", "graphql", "microservices",

    # Cyber Security
    "penetration testing", "ethical hacking",
    "network security", "owasp",

    # ERP / CRM
    "salesforce", "sap",

    # Project Management
    "agile", "scrum", "jira"
]


import re

def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in SKILLS_DB:

        pattern = r'\b' + re.escape(skill.lower()) + r'\b'

        if re.search(pattern, text):
            found_skills.append(skill)

    return sorted(list(set(found_skills)))