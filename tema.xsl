<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:foo="http://www.foo.org/" xmlns:bar="http://www.bar.org">
<xsl:template match="/">
  <html>
  <body>
  <h2>DL</h2>
    <table border="1">
      <tr bgcolor="#9acd32">
        <th>acuratete_functie</th>
      </tr>
      <xsl:for-each select="deep_learning/cuantificare_acuratete/acuratete_functie">
      <tr>
        <td><xsl:value-of select="@eroare_fata_de_ideal"/> </td>
      </tr>
      </xsl:for-each>
    </table>


    <table border="1">
      <tr bgcolor="#9acd32">
        <th>nume functie</th>
        <th>avantaj</th>
        <th>dezavantaj</th>
        <th>layer</th>
      </tr>
      <xsl:for-each select="deep_learning/functii_de_activare/functie">
      <tr>
        <td><xsl:value-of select="nume_functie"/></td>
        <td>
        <table>
            <tr>
                <td><xsl:value-of select="avantaj[position()=1]"/></td> 
                <td><xsl:value-of select="avantaj[position()=2]"/></td>
                <td><xsl:value-of select="avantaj[position()=3]"/></td>
                <td><xsl:value-of select="avantaj[position()=4]"/></td>
                <td><xsl:value-of select="avantaj[position()=5]"/></td>
                <td><xsl:value-of select="avantaj[position()=6]"/></td>
                <td><xsl:value-of select="avantaj[position()=7]"/></td>
                <td><xsl:value-of select="avantaj[position()=8]"/></td>
                <td><xsl:value-of select="avantaj[position()=9]"/></td>
                <td><xsl:value-of select="avantaj[position()=10]"/></td>
            </tr>
        </table>
        </td>


        <td>
        <table>
            <tr>
                <td><xsl:value-of select="dezavantaj[position()=1]"/></td> 
                <td><xsl:value-of select="dezavantaj[position()=2]"/></td>
                <td><xsl:value-of select="dezavantaj[position()=3]"/></td>
                <td><xsl:value-of select="dezavantaj[position()=4]"/></td>
                <td><xsl:value-of select="dezavantaj[position()=5]"/></td>
                <td><xsl:value-of select="dezavantaj[position()=6]"/></td>
                <td><xsl:value-of select="dezavantaj[position()=7]"/></td>
                <td><xsl:value-of select="dezavantaj[position()=8]"/></td>
                <td><xsl:value-of select="dezavantaj[position()=9]"/></td>
                <td><xsl:value-of select="dezavantaj[position()=10]"/></td>
            </tr>
        </table>
        </td>
        
        <td>
        <table>
        <xsl:for-each select="layer">
        <tr>
        <th><xsl:value-of select="nume_layer"/></th>
        <th><xsl:value-of select="acuratete"/></th>
        </tr>
        </xsl:for-each>
        </table>
        </td>

      </tr>
      </xsl:for-each>
    </table>

  </body>
  </html>
</xsl:template>
</xsl:stylesheet>