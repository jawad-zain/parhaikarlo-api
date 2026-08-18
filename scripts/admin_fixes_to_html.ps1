$data = Get-Content mdcat-content\verification\admin_fixes.json -Raw | ConvertFrom-Json

$rows = foreach ($q in $data) {
    $opts = @()
    foreach ($k in 'a','b','c','d') {
        if ($q.options.$k) { $opts += "<b>$($k.ToUpper())</b>: $([System.Web.HttpUtility]::HtmlEncode($q.options.$k))" }
    }
    $optHtml = $opts -join '<br>'
    $qtext = [System.Web.HttpUtility]::HtmlEncode($q.question_text)
    $reason = [System.Web.HttpUtility]::HtmlEncode($q.tiebreaker_reason)
    $bucketColor = if ($q.bucket -eq 'STORED_CORRECT') { '#e8f5e9' } else { '#fff3e0' }

    @"
<tr style="background:$bucketColor">
  <td>$($q.db_id)</td>
  <td>$($q.paper_year)</td>
  <td>$qtext<br><br>$optHtml</td>
  <td><b>$($q.stored_answer)</b></td>
  <td><b>$($q.model_answer)</b></td>
  <td><b>$($q.tiebreaker_verdict)</b><br><small>$($q.tiebreaker_confidence)</small></td>
  <td>$reason</td>
  <td>$($q.bucket)</td>
</tr>
"@
}

$html = @"
<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Admin Fixes ($($data.Count) Qs)</title>
<style>
body{font-family:system-ui,sans-serif;margin:20px;font-size:14px}
table{border-collapse:collapse;width:100%}
th,td{border:1px solid #ccc;padding:8px;vertical-align:top;text-align:left}
th{background:#333;color:#fff;position:sticky;top:0}
tr:hover{background:#f5f5f5 !important}
</style></head><body>
<h1>Admin Fixes — $($data.Count) questions</h1>
<p>Green = STORED_CORRECT (mark verified, no change). Orange = flip needed.</p>
<table>
<tr><th>DB ID</th><th>Year</th><th>Question</th><th>Stored</th><th>Gemini</th><th>Groq 70B</th><th>Reason</th><th>Bucket</th></tr>
$($rows -join "`n")
</table></body></html>
"@

Add-Type -AssemblyName System.Web
$html | Out-File mdcat-content\verification\admin_fixes.html -Encoding utf8
Write-Host "Written: mdcat-content\verification\admin_fixes.html"