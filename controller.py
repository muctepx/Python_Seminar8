import model
import logger
import view
   

def run_base():
  while True:
    mode = view.choose_mode()
    if mode == '1':
        employee = view.new_employee()
        base = logger.get_base()
        id = model.create_id(base)
        logger.add_new(employee)
    elif mode == '2':
        employee = view.contact_to_s()
        base = logger.get_base()
        result = model.search_contact(base, employee)
        view.show_found(result)
    elif mode == '3':
        employee = view.contact_to_s()
        base = logger.get_base()
        result = model.search_contact(base, employee)
        view.show_found(result)
        if "не найден" not in result[0] and len(base.split('\n')) > 1:
            result = model.search_contact(base, view.clarification())[0]
            new_employee = view.new_contact()
            upd = model.edit_employee(base, result, new_employee)
            logger.update_base(upd)
        elif "не найден" not in result[0]:
            result = base.split('\n')[0]
            new_employee = view.new_contact()
            upd = model.edit_employee(base, result, new_employee)
            logger.update_base(upd)
    elif mode =='4':
        employee = view.contact_to_s()
        base = logger.get_base()
        result = model.search_contact(base, employee)
        view.show_found(result)
        if "не найден" not in result[0] and len(base.split('\n')) > 1:
            result = model.search_contact(base, view.clarification())[0]
            upd = model.delete_employee(base, result)
            logger.update_base(upd)
        elif "не найден" not in result[0]:
            result = base.split('\n')[0]
            upd = model.delete_employee(base, result)
            logger.update_base(upd)
    else:
        view.error()