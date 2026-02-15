from pathlib import Path

def load_md_files(directory_path: Path) -> dict[str, str]:
    md_files: dict[str, str] = {}

    for file_path in list(directory_path.rglob("*.md")):
        with open(file_path, "r", encoding='utf-8') as md_file:
            md_files[file_path.name] = md_file.read()

    return md_files


def chunk_file_input(md_files: dict[str, str]) -> dict[str, list[str]]:
    result_dict: dict[str, list[str]] = {}
    for file_name, file_data in md_files.items():
        result_dict[file_name] = file_data.split(sep=None)
    
    return result_dict

# Build general word dict for future embeddings
def build_word_dict(chunk_lists: dict[str, list[str]]) -> dict[str, int]:
    word_dict: dict[str, int] = {}
    word_index = 0

    for _, word_chunks in chunk_lists.items():
        for word in word_chunks:
            if word not in word_dict:
                word_dict[word] = word_index
                word_index += 1

    return word_dict



def create_embeddings(chunk_lists: dict[str, list[str]], word_dict: dict[str, int]) -> dict[str, list[int]]:
    file_word_embeddings: dict[str, list[str, list[int]]] = {}

    for file_name, words_vector in chunk_lists.items():
        #Map to each word its embedding value
        file_word_embeddings[file_name] = list(map(lambda x: word_dict[x], words_vector))
    
    return file_word_embeddings


def filter_top_k(embeddings: dict[str, list[int]], k_limit: int = 15):
    filtered_embedding: dict[str, list[int]] = {}

    for file_name, embedding in embeddings.items():
        # For each embedding, slice K most words.
        embedding_vector_length = len(embedding)
        if embedding_vector_length < k_limit:
            filtered_embedding[file_name] = embedding[:embedding_vector_length]
        else:
            filtered_embedding[file_name] = embedding[:k_limit]


    return filtered_embedding


if __name__ == '__main__':
    current_directory = Path(__file__).parent
    loaded_files = load_md_files(current_directory)
    chunked_files = chunk_file_input(loaded_files)
    word_dictionary = build_word_dict(chunk_lists=chunked_files)
    per_file_embeddings = create_embeddings(chunked_files, word_dict=word_dictionary)
    per_file_embeddings_filtered = filter_top_k(per_file_embeddings, k_limit=50)

    print(per_file_embeddings_filtered)
