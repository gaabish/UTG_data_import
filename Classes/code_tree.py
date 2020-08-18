import uuid


class Code_tree:
    def __init__(self,
                 id,
                 code,
                 level):
        self.id = id
        self.code = code
        self.level = level

    def prepare_to_insert(self):
        return '''INSERT INTO core.code_tree (id,
                                         ancestor_id,
                                         descendant_id, 
                                         level, 
                                         root_code_id) 
                  VALUES ('{id}',
                          '{ancestor_id}',
                          '{descendant_id}',
                          {level},
                          '{root_code_id}')'''.format(id=self.id,
                                                      ancestor_id=self.code.id,
                                                      descendant_id=self.code.id,
                                                      level=self.level,
                                                      root_code_id=self.code.id)


def create_code_tree_from_line(code):
    return Code_tree(uuid.uuid4(),
                     code,
                     0)
