<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <head>
        <title>Employee List</title>
        <style> table { border-collapse: collapse; width: 50%; margin: 20px; } th, td { border: 1px solid black; padding: 10px; text-align: left; } th { background-color: #f2f2f2; } </style>
      </head>
      <body>
        <h2>Employee Details</h2>
        <table>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Department</th>
            <th>Designation</th>
            <th>Salary</th>
          </tr>
          <xsl:for-each select="employees/employee">
            <tr>
              <td>
                <xsl:value-of select="@id"/>
              </td>
              <td>
                <xsl:value-of select="name"/>
              </td>
              <td>
                <xsl:value-of select="department"/>
              </td>
              <td>
                <xsl:value-of select="designation"/>
              </td>
              <td>
                <xsl:value-of select="salary"/>
              </td>
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>