from payment_system import Payslips


def main():
    nathan = Payslips("Nathan" , "no" , 1000)
    roger = Payslips("Roger" , "no" , 3000)

    print(nathan.status() , "\n" , roger.status())

    nathan.pay()
    print("after payment")
    print(nathan.status())
    print(roger.status())
