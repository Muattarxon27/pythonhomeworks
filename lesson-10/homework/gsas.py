txt = 'abcabcdabcdeabcdefabcdefg'
done = "aouei"
ans = ""
counter = 0
for i in range(len(txt)):
    counter += 1
    ans += txt[i]
    if i!=len(txt)-1 and counter>=3 and txt[1] not in done:
        done += (txt[i])
        ans += "_"
        counter = 0
print(ans)