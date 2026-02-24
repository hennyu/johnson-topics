<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" xpath-default-namespace="http://www.tei-c.org/ns/1.0"
    exclude-result-prefixes="xs"
    version="2.0">
    
    <xsl:output method="text" encoding="UTF-8"/>
    
    
  <!-- Fehler:
    - 0826_000000.xml: nicht wohlgeformt (<summary> war nicht geschlossen) -> korrigiert
    - 0825_000000.xml: nicht wohlgeformt (<summary> war nicht geschlossen) -> korrigiert
    
    - 0744_101195.xml (1970): nicht wohlgeformt (<app>, <lem>-Schachtelungsprobleme) -> vorläufig korrigiert
    - 1028_000042.xml (1977): nicht wohlgeformt (<app>, <lem>-Schachtelungsprobleme) -> korrigiert
    - 1029_101712.xml (1977): nicht wohlgeformt (<app>, <lem>-Schachtelungsprobleme) -> korrigiert
    - 1037_101721.xml (1978): nicht wohlgeformt (<app>, <lem>-Schachtelungsprobleme) -> korrigiert
    - 1046_101732.xml (1978): nicht wohlgeformt (<app>, <lem>-Schachtelungsprobleme) -> korrigiert
    - 1048_101737.xml (1979): nicht wohlgeformt (<app>, <lem>-Schachtelungsprobleme) -> korrigiert
    - 1058_101749.xml (1979): nicht wohlgeformt (<app>, <lem>-Schachtelungsprobleme) -> korrigiert
    - 1079_101776.xml (1980): nicht wohlgeformt (<app>, <lem>-Schachtelungsprobleme) -> korrigiert
  -->
    
    <xsl:template match="/">
        <xsl:text>idno,filename,corpus,genre,sender,receiver,date,year,month,sender_norm,receiver_norm</xsl:text><xsl:text>
</xsl:text>
        <xsl:for-each select="collection('../data/letters-leipzig-xml?recurse=yes')//TEI"> <!-- [.//text[normalize-space(.)!='']] -->
            <xsl:text>uj</xsl:text><xsl:value-of select="format-number(position(),'0000')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="tokenize(base-uri(.),'/')[last()]"/>
            <xsl:text>,</xsl:text>
            <xsl:text>letters-leipzig</xsl:text>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="string-join(//classCode,' + ')"/>
            <xsl:text>,</xsl:text>
            <xsl:variable name="sender" select="string-join(//persName[@role='creator'],' + ')"/>
            <xsl:text>"</xsl:text><xsl:value-of select="$sender"/><xsl:text>"</xsl:text>
            <xsl:text>,</xsl:text>
            <xsl:variable name="receiver" select="string-join(//persName[@role='addressee'],' + ')"/>
            <xsl:text>"</xsl:text><xsl:value-of select="$receiver"/><xsl:text>"</xsl:text>
            <xsl:text>,</xsl:text>
            <xsl:variable name="date">
                <xsl:choose>
                    <xsl:when test="//creation/date[2] and //creation/date/@when"><xsl:value-of select="//creation/date[1]/@when"/></xsl:when>
                    <xsl:when test="//creation/date/@when"><xsl:value-of select="//creation/date/@when"/></xsl:when>
                    <xsl:when test="//creation/date/@from"><xsl:value-of select="//creation/date/@from"/></xsl:when>
                    <xsl:when test="//creation/date/@notAfter"><xsl:value-of select="//creation/date/@notAfter"/></xsl:when>
                    <xsl:when test="//creation/date/@notBefore"><xsl:value-of select="//creation/date/@notBefore"/></xsl:when>
                    <xsl:when test="//creation/date[contains(.,'o.D.')]">0000-00-00</xsl:when>
                    <xsl:otherwise>FEHLER</xsl:otherwise>
                </xsl:choose>
            </xsl:variable>
            <xsl:value-of select="$date"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="substring($date,1,4)"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="substring($date,6,2)"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="replace($sender,'\W','')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="replace($receiver,'\W','')"/>
            <xsl:if test="position()!=last()"><xsl:text>
</xsl:text></xsl:if>
        </xsl:for-each>
    </xsl:template>
    
</xsl:stylesheet>