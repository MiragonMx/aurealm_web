import os
import re
import yaml


def load_yaml_mapping(yaml_file):
    """Load the glossary mapping from a YAML file."""
    with open(yaml_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    people_data = data.get('people', {})
    places_data = data.get('places', {})
    things_data = data.get('things', {})
    # Flatten glossary into a word-to-link dictionary
    # Go over each glossary 'type' individually, but store in the same mapping
    mapping = {}

    if isinstance(people_data, dict):
        for entry, details in data['people'].items():
            slug = details['slug']
            for word in details['words']:
                mapping[word] = "people/" + slug
                mapping[word + 's'] = "people/" + slug

    if isinstance(places_data, dict):
        for entry, details in data['places'].items():
            slug = details['slug']
            for word in details['words']:
                mapping[word] = "places/" + slug

    if isinstance(things_data, dict):
        for entry, details in data['things'].items():
            slug = details['slug']
            for word in details['words']:
                mapping[word] = "things/" + slug

    # Sort the mapping keys by length (longest first)
    # This is to avoid linking, e.g., only 'Aldric' in an occurrence of 'Aldric von Praven'
    sorted_mapping = {k: mapping[k] for k in sorted(mapping, key=len, reverse=True)}
    return sorted_mapping


def replace_with_links(content, mapping):
    """
    Replace words/phrases with HTML links, skipping already linked text.
    Do this without changing YAML metadata of content files.
    """
    def replacement_func(match):
        matched_text = match.group(0)

        # Check if the match is already inside an HTML link
        # Look for <a href="...">matched_text</a>
        if re.search(rf'{re.escape(matched_text)}\b</a>', content):
            return matched_text  # Skip replacement
        if re.search(rf'{re.escape(matched_text)}\b">', content):
            return matched_text  # Skip replacement

        # Get the subpath for the matched word
        subpath = mapping.get(matched_text)
        if subpath:
            # Replace with an HTML link
            return rf'<a class="glossary-link" href={{{{<ref "glossary/{subpath}">}}}} >{matched_text}</a>'
        return matched_text

    # Regular expression to match YAML front matter
    yaml_pattern = r"^---\n(.*?)\n---\n"  # Matches YAML between `---` and `---`

    # Search for YAML front matter
    match = re.match(yaml_pattern, content, re.DOTALL)
    if match:
        # Extract YAML metadata and main content
        yaml_metadata = match.group(0)
        main_content = content[len(yaml_metadata):]
    else:
        # No YAML front matter found
        yaml_metadata = ""
        main_content = content

    # Build a regex pattern for all keys in the mapping
    pattern = r'\b(' + '|'.join(map(re.escape, mapping.keys())) + r')\b'

    # Apply the replacement function
    return yaml_metadata + re.sub(pattern, replacement_func, main_content)

    # for word, subpath in mapping.items():
    # # Escape special characters in the word for regex
    # esc_word = re.escape(word)
    # # Replace the word with the relative link
    # link = rf'<a class="glossary-link" href={{{{<ref "glossary/{subpath}>}}}} >{esc_word}</a>'
    # content = re.sub(
    # rf'(?<!(> |/))\b{esc_word}\b',
    # link,
    # content
    # )
    # return content


def process_files_in_directory(root_dir, mapping):
    """Recursively process all files in the directory."""
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(subdir, file)
            # Process only text-based files (e.g., .txt, .html, .md)
            if file.endswith(('.txt', '.html', '.md')):
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                # Replace words/phrases with links
                updated_content = replace_with_links(content, mapping)
                # Write the updated content back to the file
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"Processed: {file_path}")


def main():
    # Specify the YAML file and root directory
    yaml_file = 'glossary_db.yml'  # Path to the YAML file
    root_dir = './content'     # Path to the Hugo 'content' directory

    # Load the glossary mapping
    mapping = load_yaml_mapping(yaml_file)

    # Process files in the directory
    process_files_in_directory(root_dir, mapping)


if __name__ == '__main__':
    main()
