# Hashtable

> **key ──hash()──▶ integer ──mod size──▶ bucket index**

* key must be hashable

  > hash("apple")   # valid
  > hash((1, 2))    # valid
  > hash([1, 2])    # ❌ TypeError

