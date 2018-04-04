# Laptop version

import keyring

def dc(db):
    
    srv = {
        'eai': 'ltpeai',
        'ews': 'ltpews',
        'ebl': 'ltpebl',
        'mio': 'ltpmio'
    }
    srvdb = srv.get(db)
    
    cs = keyring.get_password(srvdb,'cs')
    cu = keyring.get_password(srvdb,'cu')
    cw = keyring.get_password(srvdb,'cw')
    cb = keyring.get_password(srvdb,'cb')
    return cs, cu, cw, cb
