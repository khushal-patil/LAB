<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <head>
        <title>Employee Details</title>
      </head>
      <body>
        <h2>Employee Details</h2>
        <table border="1">
          <tr>
            <th>Last Name</th>
            <th>First Name</th>
            <th>Hire Date</th>
            <th>Project ID</th>
            <th>Product</th>
            <th>Price</th>
          </tr>
          <xsl:for-each select="document/employee">
            <xsl:for-each select="projects/project">
              <tr>
                <td><xsl:value-of select="../name/lastname"/></td>
                <td><xsl:value-of select="../name/firstname"/></td>
                <td><xsl:value-of select="../hiredate"/></td>
                <td><xsl:value-of select="id"/></td>
                <td><xsl:value-of select="product"/></td>
                <td><xsl:value-of select="price"/></td>
              </tr>
            </xsl:for-each>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
