import datetime
import uuid


class Code:
    def __init__(self,
                 id,
                 delimited_value,
                 value,
                 code_type,
                 batch_id,
                 created_date,
                 gtd_number,
                 tnved_code_id,
                 trade_item_id):
        self.id = id
        self.delimited_value = delimited_value
        self.value = value
        self.code_type = code_type
        self.batch_id = batch_id
        self.created_date = created_date
        self.gtd_number = gtd_number
        self.tnved_code_id = tnved_code_id
        self.trade_item_id = trade_item_id

    def prepare_to_insert(self):
        return '''INSERT INTO core.code (id, 
                                         delimited_value, 
                                         value, 
                                         code_type, 
                                         batch_id, 
                                         created_date, 
                                         gtd_number, 
                                         tnved_code_id, 
                                         trade_item_id) 
                  VALUES ('{id}',
                          {delimited_value},
                          '{value}',
                          '{code_type}',
                          {batch_id},
                          '{created_date}',
                          {gtd_number},
                          '{tnved_code_id}',
                          '{trade_item_id}')'''.format(id=self.id,
                                                       delimited_value=self.delimited_value,
                                                       value=self.value,
                                                       code_type=self.code_type,
                                                       batch_id=self.batch_id,
                                                       created_date=self.created_date,
                                                       gtd_number=self.gtd_number,
                                                       tnved_code_id=self.tnved_code_id,
                                                       trade_item_id=self.trade_item_id)

def create_code_from_line(line_data):
    return Code(uuid.uuid4(),
                'null',
                line_data[1],
                'SGTIN',
                'null',
                datetime.datetime.now(),
                'null',
                line_data[3],
                line_data[2])
