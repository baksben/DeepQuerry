how to run "streamlit run main.py"
# DeepQuery: Advanced Knowledge Base Research Tool

## Overview

DeepQuery is an innovative research tool designed to enhance knowledge extraction and retrieval from web content. It uses state-of-the-art machine learning technologies, including LangChain, OpenAI embeddings, and FAISS, a high-performance vector database. The tool is capable of querying up to three website links simultaneously, offering deep insights and comprehensive answers. DeepQuery returns also the source where the answer was retrieved.

## Features

- **Multi-Source Processing:** Aggregate and analyze content from up to three distinct website URLs.
- **LangChain Integration:** Utilize advanced natural language understanding to process and interpret web content.
- **OpenAI Embeddings:** Leverage cutting-edge embeddings from OpenAI for accurate content representation.
- **FAISS Vector Database:** Employ a fast and efficient vector database to enhance search and retrieval operations.

## Getting Started

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/DeepQuery.git
   cd DeepQuery
   ```

2. Install the required Python packages:
pip install -r requirements.txt

3. Set up your OpenAI API key by creating a .env file in the project root and adding your API

### Usage

1. Run the Streamlit app by executing:
   ```bash
   conda activate <your_environment>
   streamlit run main.py

2. This opens a webinterface.

- On the sidebar, you input URLs directly. For example:
- - URL1: https://www.consilium.europa.eu/en/policies/sanctions/restrictive-measures-against-russia-over-ukraine/sanctions-against-russia-explained/
- - URL2: https://www.consilium.europa.eu/en/policies/sanctions/restrictive-measures-against-russia-over-ukraine/
- - URL3: https://www.bbc.com/news/world-europe-60125659

- Start the processing by clicking "Process URLs."

- The system will first split the text from your sources into manageable sections and then generate embedding vectors for each section. These embeddings help in accurately representing the text in a numerical form.

- We use FAISS, a highly efficient vector database, to store and index these embeddings. This not only speeds up the retrieval process but also enhances the overall efficiency of the search mechanism.

- The FAISS index, which contains all the embedding vectors, will be saved locally in pickle format. This makes it easy to reuse and access the index for future queries.

- Once everything is set up, you can simply pose a question and the system will fetch the most relevant answers from the indexed news articles.

## Acknowledgements

- Thanks to OpenAI for the embeddings.
- LangChain for the NLP tools.
- Facebook AI Research for developing FAISS.
- [Codebasics](https://www.youtube.com/@codebasics) for the best tutorials on langchain and LLM.


