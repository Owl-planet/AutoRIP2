open System.IO
File.WriteAllText("", "python root.py")
let msg = File.ReadAllText("")
printfn "%s" msg
// Henüz tamamlanmadı (yapım aşamasında)