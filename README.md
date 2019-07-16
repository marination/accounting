## Accounting

An accounting app that will handle sales,purchases,balancing accounts,etc.

## What to look for here?
- [System Summary](#system-summary)
- [Features](#features)
- [License](#license)


## System Summary

This system is built to simulate an accounting web application which will support creation of parties,items,accounts as well as buying,selling,transfer of money with a supported report view.

## Features
The desktop has three main sections viz. Primary,Transactions,Reports.

### Primary
It contains doctypes for easy creation of new Items, Parties and Accounts  in the ERP system along with an accounts tree view under _Chart of Accounts_.
 ### Transactions
 Here we have four transactions:
 - Purchase Invoice <br>
    You can create a purchase invoice against any supplier in your Party list and also directly make a Payment Entry or check the General Ledger right after via the buttons at the top right side. The invoice can be saved,submitted and cancelled.

- Sales Invoice <br>
    Similar to purchase invoice, this creates an invoice against customers in your Party list.The invoice can be saved,submitted and cancelled.

- Payment Entry <br>
    Complete the purchase/sales cycle by creating a payment entry. It will contain a reference to the respective invoice.The entry can be saved,submitted and cancelled.

- Journal Entry <br>
    Fiscal adjustments between accounts can be carried out by creating a journal entry. It needs a minimum of two entries in the child table.The entry can be saved,submitted and cancelled.<br>

All transactions redirect to the General Ledger.
 ### Reports
 - General Ledger Report <br>
    It contains a report view of each and every transaction carried out along with account balances. It is an immutable ledger. It also has filters at the top.

- Trial Balance <br>
    It is  a query report containing debits and credits against all accounts and their sums. This will help in identifying profits and losses as well.
#### License

This project is licensed under the MIT License 