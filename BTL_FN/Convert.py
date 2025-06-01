import csv


def csv_to_arff(input_file, output_file, relation_name, attribute_names):
    with open(input_file, 'r') as csv_file, open(output_file, 'w') as arff_file:
        # Write relation name
        arff_file.write('@relation {}\n\n'.format(relation_name))

        # Write attributes
        for name in attribute_names:
            arff_file.write('@attribute {} numeric\n'.format(name))
        arff_file.write('\n@data\n')

        # Write data
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            arff_file.write(','.join(row) + '\n')


# Thay đổi các giá trị sau đây theo nhu cầu của bạn
csv_input_file = 'input.csv'
arff_output_file = 'output.arff'
relation_name = 'your_relation_name'
attribute_names = ['attribute1', 'attribute2', 'attribute3']  # Thêm hoặc xóa các tên thuộc tính tùy ý

csv_to_arff(csv_input_file, arff_output_file, relation_name, attribute_names)