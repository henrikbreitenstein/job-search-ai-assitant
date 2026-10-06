
SENIOR_TITLE_KEYWORDS = {
    "senior",
    "lead",
    "principal",
    "staff",
    "head of",
    "director",
    "chief"
}

SKILLS = [
    "Python",
    "SQL",
    "Machine Learning",
    "Data Analysis",
    "Statistical Modeling",
    "Scikit-learn",
    "Pandas",
    "PyTorch",
    "TensorFlow",
    "Feature Engineering",
    "Model Evaluation",
    "Generative AI",
    "RAG",
    "LangChain",
    "LlamaIndex",
    "Docker",
    "Git",
    "CUDA",
    "Data Visualization",
    "Deep Learning",
    "Computer Vision",
    "Data Engineering",
    "MLOps",
    "NLP",
    "ETL",
    "NumPy",
    "Jupyter",
    "Flask",
    "REST APIs"
]

SKILL_ALIASES = {
    "Python": [
        "python", "python3", "python programming", "py"
    ],

    "SQL": [
        "sql", "postgresql", "postgres", "mysql", "sqlite",
        "sql server", "microsoft sql server", "t-sql", "tsql"
    ],

    "Machine Learning": [
        "machine learning", "ml", "maskinlæring",
        "predictive modeling", "prediktiv modellering",
        "classification", "klassifisering",
        "regression", "regresjon",
        "supervised learning", "overvåket læring",
        "unsupervised learning", "uovervåket læring"
    ],

    "Deep Learning": [
        "deep learning", "dl", "dyplæring",
        "neural networks", "nevrale nettverk"
    ],

    "Computer Vision": [
        "computer vision", "maskinsyn",
        "image analysis", "bildeanalyse",
        "image processing", "bildebehandling",
        "object detection", "objektdeteksjon",
        "segmentation", "segmentering"
    ],

    "NLP": [
        "nlp", "natural language processing",
        "språkteknologi", "tekstbehandling",
        "language models", "språkmodeller"
    ],

    "Data Analysis": [
        "data analysis", "data analytics",
        "dataanalyse", "analyse",
        "analytics", "eda",
        "exploratory data analysis"
    ],

    "Statistical Modeling": [
        "statistical modeling",
        "statistical analysis",
        "statistisk modellering",
        "statistisk analyse",
        "statistics", "statistikk",
        "hypothesis testing", "hypotesetesting",
        "regression analysis", "regresjonsanalyse"
    ],

    "Feature Engineering": [
        "feature engineering",
        "feature selection",
        "feature extraction",
        "variabelutvelgelse",
        "feature extraction",
        "data preprocessing",
        "preprosessering",
        "data transformation",
        "datatransformasjon"
    ],

    "Model Evaluation": [
        "model evaluation",
        "modelevaluering",
        "cross validation",
        "cross-validation",
        "kryssvalidering",
        "grid search",
        "gridsearchcv",
        "hyperparameter tuning",
        "hyperparameteroptimalisering",
        "roc auc",
        "pr auc",
        "precision recall",
        "confusion matrix"
    ],

    "Scikit-learn": [
        "scikit-learn", "sklearn", "scikit learn"
    ],

    "Pandas": [
        "pandas", "dataframes", "dataframe"
    ],

    "NumPy": [
        "numpy"
    ],

    "PyTorch": [
        "pytorch", "torch", "pytorch lightning", "lightning"
    ],

    "TensorFlow": [
        "tensorflow", "keras", "tf"
    ],

    "Generative AI": [
        "generative ai", "genai",
        "generativ ai",
        "large language model",
        "large language models",
        "llm", "llms",
        "foundation model",
        "foundation models",
        "prompt engineering",
        "promptutvikling"
    ],

    "RAG": [
        "rag",
        "retrieval augmented generation",
        "retrieval-augmented generation",
        "vector search",
        "semantic search",
        "vektorsøk",
        "semantisk søk",
        "vector database",
        "vektordatabase"
    ],

    "LangChain": [
        "langchain"
    ],

    "LlamaIndex": [
        "llamaindex",
        "llama-index",
        "gpt index"
    ],

    "Data Engineering": [
        "data engineering",
        "data engineer",
        "dataingeniør",
        "data engineering pipelines",
        "dataplattform",
        "data platform",
        "data warehouse",
        "data warehousing",
        "datalager"
    ],

    "ETL": [
        "etl",
        "elt",
        "data pipelines",
        "datapipelines",
        "data ingestion",
        "datainnhenting",
        "pipeline development"
    ],

    "MLOps": [
        "mlops",
        "machine learning operations",
        "model deployment",
        "modellutrulling",
        "model serving",
        "model monitoring",
        "modellovervåking"
    ],

    "Docker": [
        "docker",
        "containerization",
        "containerisering",
        "containers",
        "docker compose",
        "docker-compose"
    ],

    "Git": [
        "git",
        "github",
        "gitlab",
        "version control",
        "versionskontroll",
        "source control"
    ],

    "CUDA": [
        "cuda",
        "nvidia cuda",
        "gpu programming",
        "gpu acceleration",
        "parallel computing",
        "parallell programmering"
    ],

    "Jupyter": [
        "jupyter",
        "jupyter notebook",
        "jupyterlab"
    ],

    "Flask": [
        "flask"
    ],

    "REST APIs": [
        "rest api",
        "rest apis",
        "restful api",
        "api development",
        "api-utvikling",
        "web api"
    ],

    "Data Visualization": [
        "data visualization",
        "datavisualisering",
        "visualization",
        "visualisering",
        "matplotlib",
        "seaborn",
        "plotly",
        "dashboarding",
        "dashboards"
    ]
}

EDUCATION = [
    'Master\'s Degree',
    'Computational Science',
]

class SkillExtractor:

    def __init__(self):
        self.skills = SKILLS

    def extract(self, text):

        text = text.lower()

        found = []

        for skill, aliases in SKILL_ALIASES.items():
            
            for alias in aliases:
                if alias in text:
                    found.append(skill)
                    break

        return found


