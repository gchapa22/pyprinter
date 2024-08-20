import win32print

def get_available_printer_names():
    printer_names = []
    flags = win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS
    
    printers = win32print.EnumPrinters(flags)
    for printer in printers:
        printer_name = printer['pPrinterName']
        printer_names.append(printer_name)
    
    return printer_names

if __name__ == "__main__":
    available_printers = get_available_printer_names()
    if available_printers:
        print("Available printers:")
        for printer_name in available_printers:
            print(printer_name)
    else:
        print("No printers found.")


import win32print
import win32ui
import win32com.client
import os

def print_pdf_to_printer(printer_name, pdf_path):

    printer_handle = win32print.OpenPrinter(printer_name)
    
    try:
        default_printer_info = win32print.GetPrinter(printer_handle, 2)
        printer_info = default_printer_info.copy()
        printer_info['pDevMode'].DriverData = b'RAW'
        pdf_file = open(pdf_path, 'rb')
        printer = win32ui.CreatePrinterDC(printer_name)
        printer.StartDoc(pdf_file_path)
        printer.StartPage()
        pdf_data = pdf_file.read()
        printer.Write(pdf_data)
        printer.EndPage()
        printer.EndDoc()
        
    except Exception as e:
        print("Exception occurred: ",e)    
    
    finally:

        win32print.ClosePrinter(printer_handle)
        pdf_file.close()

if __name__ == "__main__":
    
    # Replace 'Your Printer Name' with the actual name of the printer you want to use
    selected_printer = 'Your Printer Name'
    
    # Replace this with the path to your PDF file
    pdf_file_path = "path/to/your/file.pdf"
    
    if os.path.exists(pdf_file_path):
        print(f"Printing '{pdf_file_path}' to '{selected_printer}'...")
        print_pdf_to_printer(selected_printer, pdf_file_path)
        print("Printing complete.")
    else:
        print(f"PDF file not found at '{pdf_file_path}'.")
