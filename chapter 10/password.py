import codecs
a = codecs.decode("""
    0y5g    г                    уЁ   — d d l Z d d l Z d Z d „ Z d „ Z   e j                   «       Z e j                   d «           e j                   e d ¬ «       Z
e
j                   «           e j                   e «       Z
e
j                   «           e j                   e d ¬ «       Z e j                   «           e j                   e d  d
„ ¬ «       Z e j                   «         e j#                  «         y ) й    NЪ frperg_cnffjbeqc                    уђ   — t         j                   t         d «       } | | k(  r | j                   d d ¬ «         y | j                   d d ¬ «         y ) NЪ rot_13u"   РџР°СЂРѕР»СЊ РїСЂР°РІРёР»СЊРЅС‹Р№!Ъ green) Ъ textЪ fgu    РќРµРІРµСЂРЅС‹Р№ РїР°СЂРѕР»СЊ!Ъ red) Ъ codecsЪ decodeЪ encrypted_passwordЪ config) Ъ input_passwordЪ result_labelЪ decrypted_passwords       ъ app.pyЪ check_passwordr        sE   Ђ Ь  џ ™ Ф'9ё8У DР  Ш  Р +Т +Ш  Ч  С  Р!EИ'Р  Х Rа  Ч  С  Р!AАeР  Х Lу    c                    у<   — | j                   «       } t         | | «         y © N) Ъ getr    ) Ъ entryr    Ъ
user_inputs       r    Ъ  on_submitr        s    Ђ Ш  — ‘ “ ЂJЬ  ђ:|Х ,r    u$   РџСЂРѕРіСЂР°РјРјР° СЃ РїР°СЂРѕР»РµРјu    Р’РІРµРґРёС‚Рµ РїР°СЂРѕР»СЊ:) r    Ъ u
   Р’РѕР№С‚Рёc                    у*   — t         t         t         «       S r    ) r    r    r    © r    r    ъ <lambda>r    $   s    Ђ Д9МUФT`УCaЂ r    ) r    Ъ command) r
   Ъ tkinterЪ tkr    r    r    Ъ TkЪ rootЪ titleЪ LabelЪ labelЪ packЪ Entryr    r    Ъ ButtonЪ
submit_buttonЪ mainloopr    r    r    ъ <module>r+       sА   р    Ы 
Ы  р   'Р  т   M т   -р   
Ђr‡uЃuѓwЂ Ш  ‡
Ѓ
Р 1Ф 2р     € Џ ‰ ђ Р :Ф ;Ђ Ш  ‡
Ѓ
„ р     € Џ ‰ ђ ‹ Ђ Ш  ‡
Ѓ
„ р    €rЏx‰x  2Ф &Ђ Ш  Ч  С  Ф  р    ђ —  ‘  $ \С;aФ bЂ
Ш 
Ч  С  Ф  р    ‡
Ѓ
… r    
""", "rot_13")
print(a)

print("secret_password")
