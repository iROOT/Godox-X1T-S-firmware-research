#%%
f = open('X1T-S V1.4.CEM', 'rb')
f.seek(32)
f_out = open('X1T-S V1.4.txt', 'w')
b_out = open('X1T-S V1.4.bin', 'wb')
try:
    start = 8
    end = -2
    
    for line in f:
        l = line[1:].strip().decode('utf8')
        
        out = l[:6] + '  ' + l[6:start] + '  '
                
        if len(l) == 42:
            n = 2
            out += ' '.join([l[i:i+n] for i in range(start, len(l)+end, n)])
            out += '  ' + l[end:]
            
            b_out.write(bytes.fromhex(l[start:end]))
        else:
            out += l[start:end]
            
        f_out.write(out+'\n')
finally:
    f.close()
    f_out.close()
    b_out.close()
