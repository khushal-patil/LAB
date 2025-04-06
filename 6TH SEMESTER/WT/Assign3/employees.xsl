<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html" encoding="UTF-8"/>

  <xsl:template match="/">
    <html>
      <head>
        <title>Employee Cards</title>
        <link rel="stylesheet" href="styles.css" />
      </head>
      <body>
        <h2>Infosys Employee Details</h2>
        <div class="cards-container">
          <xsl:for-each select="employees/employee">
            <xsl:variable name="index" select="position()"/>
            <xsl:variable name="class" select="concat('card', ($index mod 4) + 1)"/>
            <div>
              <xsl:attribute name="class">
                <xsl:value-of select="concat('card ', $class)"/>
              </xsl:attribute>
              <h2>
                <xsl:value-of select="$index"/>. <xsl:value-of select="name"/>
              </h2>
              <p><span class="label">Position:</span> <xsl:value-of select="designation"/></p>
              <p><span class="label">Department:</span> <xsl:value-of select="department"/></p>
              <p><span class="label">Salary:</span> <xsl:value-of select="salary"/></p>
              <p><span class="label">Hired On:</span> <xsl:value-of select="hiredate"/></p>

              <div class="projects">
                <span class="label">Projects:</span>
                <xsl:for-each select="projects/project">
                  <div class="project">
                    <xsl:value-of select="."/>
                  </div>
                </xsl:for-each>
              </div>
            </div>
          </xsl:for-each>
        </div>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
