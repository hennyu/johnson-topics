<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" xpath-default-namespace="http://www.tei-c.org/ns/1.0"
    exclude-result-prefixes="xs"
    version="2.0">
    
    <xsl:template match="/">
        
        <xsl:for-each select="collection('../data/letters-leipzig-xml?recurse=yes')//TEI">
            
            <xsl:variable name="filename" select="replace(tokenize(base-uri(.),'/')[last()],'.xml','.txt')"/>
            
            <xsl:result-document href="{concat('../data/letters-leipzig-txt/',$filename)}" encoding="UTF-8" method="text">
                <xsl:apply-templates select=".//text/body"/>
            </xsl:result-document>
            
        </xsl:for-each>
        
    </xsl:template>
    
    <!-- exclude notes -->
    <xsl:template match="note"/>
  
    <!-- exclude addresses -->
    <xsl:template match="address"/>
    
    <!-- choose lemmata and additions -->
    <xsl:template match="app">
        <xsl:choose>
            <xsl:when test="lem">
                <xsl:apply-templates select="lem"/>
            </xsl:when>
            <xsl:when test="rdg[@type='original']/subst/add">
                <xsl:apply-templates select="rdg[@type='original']/subst/add"/>
            </xsl:when>
            <xsl:when test="not(child::*)">
                <xsl:value-of select="."/>
            </xsl:when>
        </xsl:choose>
    </xsl:template>
    
    
    
    
</xsl:stylesheet>