import datetime
import uuid


class Code_transaction:
    def __init__(self,
                 id,
                 event_id,
                 code,
                 operation_date,
                 location_id,
                 owner_id,
                 receiver_location_id,
                 receiver_company_id,
                 accept_status,
                 base_status,
                 regulator_status,
                 legal_entity_id,
                 parent_transaction_id,
                 type,
                 created_date,
                 reserved):
        self.id = id
        self.event_id = event_id
        self.code = code
        self.operation_date = operation_date
        self.location_id = location_id
        self.owner_id = owner_id
        self.receiver_location_id = receiver_location_id
        self.receiver_company_id = receiver_company_id
        self.accept_status = accept_status
        self.base_status = base_status
        self.regulator_status = regulator_status
        self.legal_entity_id = legal_entity_id
        self.parent_transaction_id = parent_transaction_id
        self.type = type
        self.created_date = created_date
        self.reserved = reserved

    def prepare_to_insert(self):
        return '''INSERT INTO core.code_transaction (id,
                                                event_id,
                                                code_id,
                                                parent_code_id,
                                                operation_date,
                                                location_id,
                                                owner_id,
                                                receiver_location_id,
                                                receiver_company_id,
                                                accept_status,
                                                base_status,
                                                regulator_status,
                                                legal_entity_id,
                                                parent_transaction_id,
                                                type,
                                                created_date,
                                                reserved) 
                  VALUES ('{id}',
                          '{event_id}',
                          '{code_id}',
                          '{parent_code_id}',
                          '{operation_date}',
                          '{location_id}',
                          '{owner_id}',
                          '{receiver_location_id}',
                          '{receiver_company_id}',
                          '{accept_status}',
                          '{base_status}',
                          '{regulator_status}',
                          '{legal_entity_id}',
                          {parent_transaction_id},
                          '{type}',
                          '{created_date}',
                          {reserved})'''.format(id=self.id,
                                                event_id=self.event_id,
                                                code_id=self.code.id,
                                                parent_code_id=self.code.id,
                                                operation_date=self.operation_date,
                                                location_id=self.location_id,
                                                owner_id=self.owner_id,
                                                receiver_location_id=self.receiver_location_id,
                                                receiver_company_id=self.receiver_company_id,
                                                accept_status=self.accept_status,
                                                base_status=self.base_status,
                                                regulator_status=self.regulator_status,
                                                legal_entity_id=self.legal_entity_id,
                                                parent_transaction_id=self.parent_transaction_id,
                                                type=self.type,
                                                created_date=self.created_date,
                                                reserved=self.reserved)


def create_code_transaction_from_line(line_data, code):
    return Code_transaction(uuid.uuid4(),
                            '7b671a81-3ad7-4007-b0cb-4c22933b39f5',
                            code,
                            datetime.datetime.now(),
                            line_data[5],
                            line_data[6],
                            line_data[0],
                            line_data[7],
                            line_data[8],
                            line_data[10],
                            line_data[9],
                            line_data[4],
                            'null',
                            'CREATE',
                            datetime.datetime.now(),
                            line_data[11])
