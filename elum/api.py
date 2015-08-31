from Bio import Entrez
import pyprind


def complete_me(content_as_list, output_filename, email):
    """
    Add metadata to the blast output file. Metadata is obtained by querying the
    NCBI database.

    :param content_as_list: blast output content (CSV file) as list of lines.
    :param output_filename: write line by line.
    """
    Entrez.email = email

    for i in pyprind.prog_bar(range(len(content_as_list))):
        line = content_as_list[i]
        line = line.strip()
        if line.startswith('query'):
            with open(output_filename, 'w') as handle:
                handle.write(line + '\tGeneLength\tTitle\n')
            continue

        line_complement = _get_metadata_as_string(line)

        with open(output_filename, 'a') as handle:
            handle.write(line + '\t' + line_complement + '\n')


def _get_metadata_as_string(line):
    """
    Takes a line of the blast output CSV file, extracts the GI (genbank idendifier)
    and returns the extra metadata as string.

    :param line:
    :return:
    """
    line_as_fields = line.split('\t')
    identifier_column = line_as_fields[1].split('|')

    gi = identifier_column[1]
    metadata = _query_ncbi(gi)
    line_complement = _convert_metadata_to_line(metadata)

    return line_complement


def _query_ncbi(gi):
    """

    :param gi: NCBI identifier
    :return: metadata as dict
    """
    handle = Entrez.esummary(db="nucleotide", id=gi, retmode="text")
    record = Entrez.read(handle)
    handle.close()
    return record[0]


def _convert_metadata_to_line(metadata):
    out = ''
    try:
        out += str(metadata['Length']) + '\t'
    except KeyError:
        out += '\t'

    try:
        out += metadata['Title']
    except KeyError:
        pass

    return out
