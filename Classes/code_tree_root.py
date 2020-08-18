import uuid


class Code_tree_root:
    def __init__(self,
                 id,
                 legal_entity_id,
                 code,
                 location_id,
                 owner_id,
                 receiver_location_id,
                 receiver_company_id,
                 accept_status,
                 base_status,
                 regulator_status,
                 reserved,
                 code_transaction,
                 operation_date):
        self.id = id
        self.legal_entity_id = legal_entity_id
        self.code = code
        self.location_id = location_id
        self.owner_id = owner_id
        self.receiver_location_id = receiver_location_id
        self.receiver_company_id = receiver_company_id
        self.accept_status = accept_status
        self.base_status = base_status
        self.regulator_status = regulator_status
        self.reserved = reserved
        self.code_transaction = code_transaction
        self.operation_date = operation_date

    def prepare_to_insert(self):
        return '''INSERT INTO core.code_tree_root (id,
                                              legal_entity_id,
                                              code_id,
                                              location_id,
                                              owner_id,
                                              receiver_location_id,
                                              receiver_company_id,
                                              accept_status,
                                              base_status,
                                              regulator_status,
                                              reserved,
                                              last_transaction_id,
                                              operation_date) 
                  VALUES ('{id}',
                          '{legal_entity_id}',
                          '{code_id}',
                          '{location_id}',
                          '{owner_id}',
                          '{receiver_location_id}',
                          '{receiver_company_id}',
                          '{accept_status}',
                          '{base_status}',
                          '{regulator_status}',
                          {reserved},
                          '{last_transaction_id}',
                          '{operation_date}')'''.format(id=self.id,
                                                        legal_entity_id=self.legal_entity_id,
                                                        code_id=self.code.id,
                                                        location_id=self.location_id,
                                                        owner_id=self.owner_id,
                                                        receiver_location_id=self.receiver_location_id,
                                                        receiver_company_id=self.receiver_company_id,
                                                        accept_status=self.accept_status,
                                                        base_status=self.base_status,
                                                        regulator_status=self.regulator_status,
                                                        reserved=self.reserved,
                                                        last_transaction_id=self.code_transaction.id,
                                                        operation_date=self.operation_date)


def create_code_tree_root_from_line(line_data, code, code_transaction):
    return Code_tree_root(uuid.uuid4(),
                          line_data[4],
                          code,
                          line_data[5],
                          line_data[6],
                          line_data[0],
                          line_data[7],
                          line_data[8],
                          line_data[10],
                          line_data[9],
                          line_data[11],
                          code_transaction,
                          line_data[12])
