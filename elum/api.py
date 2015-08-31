from Bio import Entrez


def convert_metadata_to_line(metadata):
    out = ''
    try:
        out += metadata['Title']
    except KeyError:
        out += '\t'

    try:
        out += str(metadata['Length'])
    except KeyError:
        out += '\t'

    return out


def query_ncbi(gi):
    """

    :param gi: NCBI identifier
    :return: metadata as dict
    """
    handle = Entrez.esummary(db="nucleotide", id=gi, retmode="text")
    record = Entrez.read(handle)
    handle.close()
    return record[0]


def complete_me(content_as_list, email):
    """
    Add metadata to the blast output file. Metadata is obtained by querying the
    NCBI database.

    :param content_as_list: blast output content (CSV file) as list of lines.
    :return: string with the completed metadata.
    """
    Entrez.email = email

    output = []
    append = output.append

    for line in content_as_list:
        line = line.strip()
        if line.startswith('query'):
            append(line + '\t' + 'Title\tGeneLength')
            continue

        line_as_fields = line.split('\t')
        identifier_column = line_as_fields[1].split('|')
        gi = identifier_column[1]
        metadata = query_ncbi(gi)
        line_complement = convert_metadata_to_line(metadata)
        append(line + '\t' + line_complement)
        break
    print('\n'.join(output))
